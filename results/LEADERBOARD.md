# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 349 windows, 9378 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 7:15 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 675 | 41.6 | 42.0 | $-320.46 | -4.7% | $679.54 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 928 | 52.0 | 52.0 | $-374.74 | -4.0% | $625.26 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 762 | 51.3 | 52.1 | $-393.38 | -5.2% | $606.62 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 762 | 48.7 | 49.6 | $-467.75 | -6.1% | $532.25 | -1.7 | done | can't tell from luck |
| trend_filter | 516 | 47.3 | 50.2 | $-513.64 | -10.0% | $486.36 | -2.3 | done | losing for real |
| coinflip | 1389 | 50.3 | 50.8 | $-657.49 | -4.7% | $342.51 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 928 | 48.0 | 49.7 | $-689.25 | -7.4% | $310.75 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1389 | 48.9 | 51.4 | $-1166.00 | -8.4% | $-166.00 | -3.2 | done | losing for real |
| always_up | 1389 | 46.5 | 50.6 | $-1627.60 | -11.7% | $-627.60 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2105 | 47.1 | 49.3 | $-1722.56 |
| ETH | 2361 | 47.5 | 48.7 | $-1718.89 |
| SOL | 2430 | 48.0 | 49.3 | $-1806.45 |
| XRP | 2482 | 48.8 | 49.1 | $-1190.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
