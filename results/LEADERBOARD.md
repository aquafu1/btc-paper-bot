# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 718 windows, 19789 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2026 | 51.6 | 50.8 | $-526.87 | -2.6% | $473.13 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 1661 | 50.1 | 49.5 | $-562.73 | -3.4% | $437.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 912 | 38.0 | 39.1 | $-592.90 | -6.5% | $407.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1373 | 40.7 | 41.1 | $-658.40 | -4.8% | $341.60 | -1.5 | done | can't tell from luck |
| trend_filter | 1159 | 50.2 | 50.9 | $-664.29 | -5.7% | $335.71 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1661 | 49.9 | 51.3 | $-1220.01 | -7.3% | $-220.01 | -3.1 | done | losing for real |
| coinflip | 2864 | 50.2 | 50.3 | $-1231.60 | -4.3% | $-231.60 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2026 | 48.4 | 50.0 | $-1419.39 | -7.0% | $-419.39 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2864 | 51.1 | 51.8 | $-1427.92 | -5.0% | $-427.92 | -2.8 | done | losing for real |
| always_up | 2864 | 47.3 | 49.5 | $-2437.40 | -8.5% | $-1437.40 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4481 | 48.1 | 49.1 | $-2742.11 |
| ETH | 4927 | 48.3 | 48.5 | $-2906.83 |
| SOL | 5160 | 48.2 | 48.7 | $-3030.73 |
| XRP | 5221 | 48.6 | 48.4 | $-2375.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
