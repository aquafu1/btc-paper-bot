# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 659 windows, 18223 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1542 | 50.6 | 49.7 | $-365.45 | -2.4% | $634.55 | -0.9 | done | can't tell from luck |
| trend_filter | 1059 | 50.6 | 51.0 | $-529.55 | -5.0% | $470.45 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1869 | 51.5 | 50.9 | $-553.32 | -3.0% | $446.68 | -1.3 | done | can't tell from luck |
| value_ev10 | 839 | 38.1 | 39.5 | $-625.05 | -7.4% | $374.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1267 | 40.7 | 41.4 | $-700.41 | -5.5% | $299.59 | -1.7 | done | can't tell from luck |
| coinflip | 2631 | 50.1 | 50.5 | $-1175.39 | -4.5% | $-175.39 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1542 | 49.4 | 51.3 | $-1240.45 | -8.0% | $-240.45 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1869 | 48.5 | 50.1 | $-1273.58 | -6.8% | $-273.58 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2631 | 50.9 | 51.8 | $-1356.65 | -5.2% | $-356.65 | -2.7 | done | losing for real |
| always_up | 2631 | 47.7 | 49.8 | $-2148.94 | -8.2% | $-1148.94 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4133 | 48.4 | 49.3 | $-2438.21 |
| ETH | 4545 | 48.3 | 48.7 | $-2738.00 |
| SOL | 4747 | 48.2 | 48.8 | $-2810.98 |
| XRP | 4798 | 48.6 | 48.6 | $-2249.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
