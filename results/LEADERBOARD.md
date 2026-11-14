# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 317 windows, 8495 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 692 | 53.3 | 51.7 | $-74.25 | -1.1% | $925.75 | -0.3 | done | can't tell from luck |
| value_ev20 | 160 | 34.4 | 36.7 | $-182.09 | -11.4% | $817.91 | -1.1 | Sun 12:00 AM | too few trades (160/200) |
| reversal_15m_0.10pct | 842 | 52.6 | 51.9 | $-243.62 | -2.9% | $756.38 | -0.9 | done | can't tell from luck |
| value_ev10 | 408 | 38.2 | 40.5 | $-399.41 | -9.8% | $600.59 | -1.7 | done | can't tell from luck |
| value_ev5 | 608 | 39.8 | 42.2 | $-603.78 | -9.9% | $396.22 | -2.2 | done | losing for real |
| trend_filter | 471 | 44.6 | 50.4 | $-738.46 | -15.7% | $261.54 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 842 | 47.4 | 49.8 | $-756.22 | -9.0% | $243.78 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 692 | 46.7 | 49.9 | $-764.76 | -11.1% | $235.24 | -3.0 | done | losing for real |
| coinflip | 1260 | 49.8 | 51.0 | $-819.17 | -6.5% | $180.83 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1260 | 48.3 | 51.3 | $-1271.53 | -10.1% | $-271.53 | -3.7 | done | losing for real |
| always_up | 1260 | 47.3 | 50.5 | $-1306.06 | -10.4% | $-306.06 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1904 | 46.3 | 49.3 | $-1959.10 |
| ETH | 2133 | 46.8 | 48.8 | $-2075.97 |
| SOL | 2211 | 47.8 | 49.4 | $-1832.84 |
| XRP | 2247 | 48.6 | 49.1 | $-1291.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
