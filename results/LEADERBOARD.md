# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 717 windows, 19778 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2025 | 51.6 | 50.8 | $-516.87 | -2.6% | $483.13 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 1660 | 50.1 | 49.5 | $-552.73 | -3.3% | $447.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 912 | 38.0 | 39.1 | $-592.90 | -6.5% | $407.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1373 | 40.7 | 41.1 | $-658.40 | -4.8% | $341.60 | -1.5 | done | can't tell from luck |
| trend_filter | 1158 | 50.2 | 50.9 | $-671.90 | -5.8% | $328.10 | -2.0 | done | losing for real |
| coinflip | 2862 | 50.2 | 50.3 | $-1211.60 | -4.2% | $-211.60 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1660 | 49.9 | 51.3 | $-1232.34 | -7.4% | $-232.34 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2862 | 51.1 | 51.8 | $-1425.53 | -5.0% | $-425.53 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2025 | 48.4 | 50.0 | $-1431.72 | -7.1% | $-431.72 | -3.2 | done | losing for real |
| always_up | 2862 | 47.3 | 49.5 | $-2439.73 | -8.5% | $-1439.73 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4477 | 48.1 | 49.1 | $-2737.33 |
| ETH | 4920 | 48.3 | 48.5 | $-2903.81 |
| SOL | 5160 | 48.2 | 48.7 | $-3030.73 |
| XRP | 5221 | 48.6 | 48.4 | $-2375.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
