# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 998 windows, 27732 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 512 | 34.2 | 35.0 | $-303.44 | -5.9% | $696.57 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2828 | 51.1 | 50.4 | $-816.85 | -2.9% | $183.15 | -1.5 | done | can't tell from luck |
| value_ev10 | 1269 | 37.5 | 39.1 | $-903.92 | -7.1% | $96.08 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2380 | 49.7 | 49.7 | $-1126.46 | -4.7% | $-126.46 | -2.3 | done | losing for real |
| value_ev5 | 1922 | 39.6 | 41.0 | $-1254.47 | -6.5% | $-254.47 | -2.4 | done | losing for real |
| trend_filter | 1661 | 49.4 | 50.8 | $-1264.66 | -7.6% | $-264.66 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2380 | 50.3 | 50.9 | $-1529.38 | -6.4% | $-529.38 | -3.2 | done | losing for real |
| coinflip | 3984 | 50.3 | 50.3 | $-1741.53 | -4.4% | $-741.53 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2828 | 48.9 | 50.3 | $-1974.40 | -7.0% | $-974.40 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3984 | 50.6 | 51.5 | $-2252.48 | -5.7% | $-1252.48 | -3.7 | done | losing for real |
| always_up | 3984 | 46.9 | 49.5 | $-3880.05 | -9.7% | $-2880.05 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6323 | 48.2 | 49.1 | $-3594.26 |
| ETH | 6890 | 48.0 | 48.5 | $-4507.25 |
| SOL | 7250 | 48.1 | 48.6 | $-4249.65 |
| XRP | 7269 | 48.0 | 48.4 | $-4696.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
