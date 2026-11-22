# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1095 windows, 30299 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 571 | 34.7 | 35.0 | $-310.36 | -5.4% | $689.64 | -1.0 | done | can't tell from luck |
| value_ev10 | 1404 | 38.2 | 39.1 | $-813.68 | -5.8% | $186.32 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3061 | 51.0 | 50.5 | $-916.01 | -3.0% | $83.99 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2577 | 49.6 | 49.4 | $-1124.77 | -4.4% | $-124.77 | -2.2 | done | losing for real |
| value_ev5 | 2134 | 40.1 | 41.0 | $-1173.29 | -5.5% | $-173.29 | -2.1 | done | losing for real |
| trend_filter | 1798 | 49.3 | 50.5 | $-1321.80 | -7.4% | $-321.80 | -3.2 | done | losing for real |
| coinflip | 4372 | 50.5 | 50.2 | $-1610.62 | -3.7% | $-610.62 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2577 | 50.4 | 51.1 | $-1622.59 | -6.3% | $-622.59 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3061 | 49.0 | 50.2 | $-1968.80 | -6.4% | $-968.80 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4372 | 50.8 | 51.4 | $-2209.99 | -5.1% | $-1209.99 | -3.4 | done | losing for real |
| always_up | 4372 | 47.5 | 49.3 | $-3481.00 | -8.0% | $-2481.00 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6930 | 48.5 | 49.0 | $-3321.41 |
| ETH | 7508 | 48.2 | 48.4 | $-4384.52 |
| SOL | 7894 | 48.1 | 48.4 | $-4361.13 |
| XRP | 7967 | 48.3 | 48.2 | $-4485.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
