# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1424 windows, 36434 settled trades, 457 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 730 | 34.8 | 35.3 | $-465.63 | -6.4% | $534.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1766 | 38.9 | 39.2 | $-757.88 | -4.3% | $242.12 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3639 | 50.9 | 50.1 | $-1009.80 | -2.8% | $-9.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 2667 | 40.6 | 41.1 | $-1232.32 | -4.6% | $-232.32 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 3058 | 49.2 | 49.3 | $-1488.56 | -4.9% | $-488.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3058 | 50.8 | 50.9 | $-1568.23 | -5.1% | $-568.23 | -2.9 | done | losing for real |
| trend_filter | 2163 | 48.5 | 50.3 | $-1893.07 | -8.8% | $-893.07 | -4.2 | done | losing for real |
| coinflip | 5238 | 50.1 | 50.0 | $-2210.81 | -4.2% | $-1210.81 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3639 | 49.1 | 50.2 | $-2247.09 | -6.2% | $-1247.09 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5238 | 50.1 | 51.3 | $-3262.85 | -6.2% | $-2262.85 | -4.6 | done | losing for real |
| always_up | 5238 | 48.0 | 49.3 | $-3631.88 | -6.9% | $-2631.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9216 | 48.1 | 48.8 | $-4912.37 |
| ETH | 9908 | 48.1 | 48.0 | $-5271.53 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
