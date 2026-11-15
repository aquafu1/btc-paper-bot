# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 386 windows, 10543 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 10:45 PM | too few trades (196/200) |
| value_ev10 | 506 | 39.9 | 40.5 | $-225.02 | -4.4% | $774.98 | -0.8 | done | can't tell from luck |
| value_ev5 | 747 | 41.6 | 42.1 | $-344.11 | -4.6% | $655.89 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 887 | 49.9 | 49.8 | $-369.85 | -4.2% | $630.15 | -1.3 | done | can't tell from luck |
| trend_filter | 590 | 48.6 | 50.6 | $-482.30 | -8.2% | $517.70 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1058 | 48.9 | 49.8 | $-580.11 | -5.5% | $419.89 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1058 | 51.1 | 52.1 | $-614.18 | -5.8% | $385.82 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 887 | 50.1 | 52.0 | $-688.17 | -7.8% | $311.83 | -2.4 | done | losing for real |
| coinflip | 1538 | 49.9 | 50.8 | $-833.20 | -5.4% | $166.80 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1538 | 49.4 | 51.6 | $-1184.38 | -7.7% | $-184.38 | -3.1 | done | losing for real |
| always_up | 1538 | 45.8 | 50.7 | $-2036.71 | -13.2% | $-1036.71 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2376 | 47.4 | 49.4 | $-1843.39 |
| ETH | 2645 | 47.6 | 48.9 | $-1919.81 |
| SOL | 2734 | 47.9 | 49.5 | $-2100.14 |
| XRP | 2788 | 48.6 | 49.2 | $-1521.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
