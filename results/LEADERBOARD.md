# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 319 windows, 8543 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 692 | 53.3 | 51.7 | $-74.25 | -1.1% | $925.75 | -0.3 | done | can't tell from luck |
| value_ev20 | 160 | 34.4 | 36.7 | $-182.09 | -11.4% | $817.91 | -1.1 | Sun 12:45 AM | too few trades (160/200) |
| reversal_15m_0.10pct | 850 | 52.8 | 52.0 | $-217.87 | -2.6% | $782.13 | -0.8 | done | can't tell from luck |
| value_ev10 | 409 | 38.1 | 40.5 | $-409.41 | -10.0% | $590.59 | -1.7 | done | can't tell from luck |
| value_ev5 | 613 | 39.8 | 42.2 | $-609.40 | -9.9% | $390.60 | -2.2 | done | losing for real |
| trend_filter | 473 | 44.6 | 50.3 | $-736.41 | -15.6% | $263.59 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 692 | 46.7 | 49.9 | $-764.76 | -11.1% | $235.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 850 | 47.2 | 49.8 | $-791.84 | -9.3% | $208.16 | -2.7 | done | losing for real |
| coinflip | 1268 | 49.8 | 51.0 | $-806.15 | -6.4% | $193.85 | -2.3 | done | losing for real |
| always_up | 1268 | 47.5 | 50.4 | $-1268.61 | -10.0% | $-268.61 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 1268 | 48.2 | 51.3 | $-1291.95 | -10.2% | $-291.95 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1916 | 46.2 | 49.3 | $-2007.90 |
| ETH | 2146 | 46.7 | 48.8 | $-2121.64 |
| SOL | 2223 | 48.0 | 49.4 | $-1766.83 |
| XRP | 2258 | 48.6 | 49.1 | $-1256.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
