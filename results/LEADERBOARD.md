# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 936 windows, 25900 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1170 | 37.9 | 39.1 | $-703.12 | -6.0% | $296.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2647 | 51.0 | 50.6 | $-890.74 | -3.4% | $109.26 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2212 | 50.1 | 49.9 | $-940.23 | -4.3% | $59.77 | -2.0 | done | losing for real |
| trend_filter | 1539 | 50.0 | 51.0 | $-1050.73 | -6.8% | $-50.73 | -2.8 | done | losing for real |
| value_ev5 | 1780 | 39.6 | 41.0 | $-1159.62 | -6.5% | $-159.62 | -2.3 | done | losing for real |
| coinflip | 3739 | 50.5 | 50.4 | $-1525.36 | -4.1% | $-525.36 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2212 | 49.9 | 50.9 | $-1549.31 | -7.0% | $-549.31 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2647 | 49.0 | 50.3 | $-1711.55 | -6.5% | $-711.55 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3739 | 51.0 | 51.6 | $-1891.57 | -5.1% | $-891.57 | -3.2 | done | losing for real |
| always_up | 3739 | 46.7 | 49.7 | $-3864.32 | -10.3% | $-2864.32 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5905 | 48.1 | 49.1 | $-3491.14 |
| ETH | 6433 | 48.2 | 48.6 | $-4020.34 |
| SOL | 6760 | 48.2 | 48.6 | $-4001.62 |
| XRP | 6802 | 48.3 | 48.5 | $-3929.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
