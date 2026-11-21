# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1004 windows, 27924 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 516 | 34.3 | 35.0 | $-292.56 | -5.7% | $707.44 | -1.0 | done | can't tell from luck |
| value_ev10 | 1279 | 37.5 | 39.1 | $-904.13 | -7.1% | $95.87 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2844 | 51.0 | 50.4 | $-910.00 | -3.2% | $90.00 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2401 | 50.0 | 49.7 | $-1000.71 | -4.2% | $-0.71 | -2.0 | done | losing for real |
| trend_filter | 1672 | 49.6 | 50.8 | $-1210.99 | -7.2% | $-210.99 | -3.0 | done | losing for real |
| value_ev5 | 1940 | 39.6 | 41.0 | $-1272.38 | -6.6% | $-272.38 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2401 | 50.0 | 50.9 | $-1668.76 | -7.0% | $-668.76 | -3.5 | done | losing for real |
| coinflip | 4009 | 50.4 | 50.4 | $-1707.16 | -4.3% | $-707.16 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2844 | 49.0 | 50.3 | $-1891.45 | -6.7% | $-891.45 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4009 | 50.7 | 51.6 | $-2247.53 | -5.6% | $-1247.53 | -3.7 | done | losing for real |
| always_up | 4009 | 47.1 | 49.6 | $-3752.59 | -9.4% | $-2752.59 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6372 | 48.2 | 49.0 | $-3659.56 |
| ETH | 6932 | 48.0 | 48.5 | $-4474.19 |
| SOL | 7298 | 48.2 | 48.6 | $-4093.87 |
| XRP | 7322 | 48.1 | 48.4 | $-4630.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
