# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 195 windows, 4997 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 488 | 58.6 | 52.6 | $+396.50 | +8.1% | $1396.50 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 364 | 59.6 | 53.0 | $+332.94 | +9.1% | $1332.94 | +1.9 | done | can't tell from luck |
| value_ev20 | 96 | 31.2 | 37.1 | $-208.58 | -21.7% | $791.42 | -1.8 | Sun 6:15 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 772 | 51.3 | 51.3 | $-334.74 | -4.3% | $665.26 | -1.3 | done | can't tell from luck |
| coinflip | 772 | 50.5 | 51.0 | $-429.17 | -5.6% | $570.83 | -1.6 | done | can't tell from luck |
| value_ev10 | 258 | 35.7 | 40.9 | $-451.04 | -17.5% | $548.96 | -2.5 | done | losing for real |
| trend_filter | 248 | 41.5 | 49.4 | $-473.74 | -19.1% | $526.26 | -3.0 | done | losing for real |
| value_ev5 | 375 | 38.1 | 42.6 | $-558.15 | -14.9% | $441.85 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 364 | 40.4 | 49.1 | $-781.84 | -21.5% | $218.16 | -4.2 | done | losing for real |
| always_up | 772 | 46.2 | 50.3 | $-975.47 | -12.6% | $24.53 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 488 | 41.4 | 49.6 | $-976.74 | -20.0% | $23.26 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1096 | 45.8 | 49.5 | $-1198.04 |
| ETH | 1241 | 45.9 | 48.9 | $-1432.01 |
| SOL | 1298 | 47.8 | 49.1 | $-1128.87 |
| XRP | 1362 | 49.3 | 49.2 | $-701.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
