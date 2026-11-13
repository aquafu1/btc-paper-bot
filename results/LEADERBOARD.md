# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 191 windows, 4883 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 475 | 58.1 | 52.5 | $+356.92 | +7.5% | $1356.92 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 357 | 59.9 | 53.1 | $+347.19 | +9.7% | $1347.19 | +2.0 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 5:15 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 756 | 52.0 | 51.4 | $-231.21 | -3.1% | $768.79 | -0.9 | done | can't tell from luck |
| value_ev10 | 248 | 36.3 | 40.8 | $-393.19 | -15.9% | $606.81 | -2.2 | done | losing for real |
| coinflip | 756 | 50.5 | 51.0 | $-407.89 | -5.4% | $592.11 | -1.5 | done | can't tell from luck |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 365 | 38.6 | 42.6 | $-500.29 | -13.7% | $499.71 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 357 | 40.1 | 49.0 | $-778.37 | -21.8% | $221.63 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 475 | 41.9 | 49.7 | $-903.22 | -19.0% | $96.78 | -4.2 | done | losing for real |
| always_up | 756 | 46.4 | 50.2 | $-918.35 | -12.1% | $81.65 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1071 | 46.0 | 49.6 | $-1101.81 |
| ETH | 1214 | 46.0 | 48.8 | $-1360.44 |
| SOL | 1265 | 47.8 | 49.1 | $-1074.73 |
| XRP | 1333 | 49.7 | 49.2 | $-547.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
