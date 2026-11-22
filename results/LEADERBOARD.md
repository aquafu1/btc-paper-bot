# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1092 windows, 30216 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 570 | 34.6 | 35.0 | $-327.96 | -5.8% | $672.04 | -1.0 | done | can't tell from luck |
| value_ev10 | 1399 | 38.0 | 39.1 | $-888.24 | -6.3% | $111.76 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3053 | 51.0 | 50.5 | $-922.51 | -3.0% | $77.49 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2570 | 49.6 | 49.4 | $-1123.09 | -4.4% | $-123.09 | -2.2 | done | losing for real |
| value_ev5 | 2125 | 40.0 | 41.0 | $-1251.11 | -5.9% | $-251.11 | -2.3 | done | losing for real |
| trend_filter | 1796 | 49.4 | 50.4 | $-1301.80 | -7.2% | $-301.80 | -3.1 | done | losing for real |
| coinflip | 4360 | 50.6 | 50.2 | $-1617.46 | -3.7% | $-617.46 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2570 | 50.4 | 51.1 | $-1646.35 | -6.4% | $-646.35 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3053 | 49.0 | 50.2 | $-1977.75 | -6.5% | $-977.75 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4360 | 50.9 | 51.4 | $-2166.56 | -5.0% | $-1166.56 | -3.4 | done | losing for real |
| always_up | 4360 | 47.5 | 49.3 | $-3567.04 | -8.2% | $-2567.04 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6905 | 48.5 | 49.0 | $-3397.78 |
| ETH | 7488 | 48.2 | 48.4 | $-4407.29 |
| SOL | 7873 | 48.1 | 48.4 | $-4488.95 |
| XRP | 7950 | 48.3 | 48.2 | $-4495.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
