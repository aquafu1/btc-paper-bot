# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1609 windows, 38867 settled trades, 398 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 821 | 34.2 | 35.2 | $-645.00 | -7.9% | $355.00 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3835 | 50.9 | 50.0 | $-993.42 | -2.6% | $6.58 | -1.6 | done | can't tell from luck |
| value_ev10 | 1941 | 38.4 | 39.0 | $-1065.80 | -5.5% | $-65.80 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3211 | 51.0 | 50.9 | $-1475.93 | -4.6% | $-475.93 | -2.7 | done | losing for real |
| value_ev5 | 2906 | 40.4 | 41.0 | $-1503.27 | -5.2% | $-503.27 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3211 | 49.0 | 49.2 | $-1743.64 | -5.4% | $-743.64 | -3.1 | done | losing for real |
| trend_filter | 2283 | 48.5 | 50.4 | $-2033.23 | -8.9% | $-1033.23 | -4.4 | done | losing for real |
| coinflip | 5608 | 50.1 | 49.9 | $-2338.99 | -4.2% | $-1338.99 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3835 | 49.1 | 50.2 | $-2369.91 | -6.2% | $-1369.91 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5608 | 50.2 | 51.3 | $-3482.17 | -6.2% | $-2482.17 | -4.8 | done | losing for real |
| always_up | 5608 | 48.2 | 49.1 | $-3589.18 | -6.4% | $-2589.18 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10360 | 48.0 | 48.6 | $-5852.03 |
| ETH | 11197 | 48.0 | 47.7 | $-5804.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
