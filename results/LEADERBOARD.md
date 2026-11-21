# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 952 windows, 26423 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1200 | 38.1 | 39.1 | $-668.29 | -5.6% | $331.71 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2703 | 51.3 | 50.6 | $-771.71 | -2.9% | $228.29 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2258 | 50.2 | 49.7 | $-864.10 | -3.8% | $135.90 | -1.8 | done | can't tell from luck |
| trend_filter | 1580 | 50.0 | 50.8 | $-1023.02 | -6.5% | $-23.02 | -2.6 | done | losing for real |
| value_ev5 | 1822 | 39.8 | 41.0 | $-1060.24 | -5.8% | $-60.24 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2258 | 49.8 | 51.0 | $-1637.20 | -7.3% | $-637.20 | -3.5 | done | losing for real |
| coinflip | 3804 | 50.2 | 50.4 | $-1727.97 | -4.5% | $-727.97 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2703 | 48.7 | 50.2 | $-1882.27 | -7.0% | $-882.27 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3804 | 50.9 | 51.5 | $-1925.74 | -5.1% | $-925.74 | -3.2 | done | losing for real |
| always_up | 3804 | 46.8 | 49.6 | $-3809.69 | -10.0% | $-2809.69 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6022 | 48.1 | 49.0 | $-3461.03 |
| ETH | 6569 | 48.1 | 48.5 | $-4071.25 |
| SOL | 6890 | 48.2 | 48.6 | $-3846.17 |
| XRP | 6942 | 48.2 | 48.5 | $-4146.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
