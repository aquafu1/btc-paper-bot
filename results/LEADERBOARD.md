# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 377 windows, 10245 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 8:15 PM | too few trades (196/200) |
| value_ev10 | 500 | 40.0 | 40.4 | $-209.12 | -4.2% | $790.88 | -0.8 | done | can't tell from luck |
| value_ev5 | 737 | 41.7 | 42.1 | $-332.45 | -4.5% | $667.55 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 852 | 49.6 | 49.7 | $-392.24 | -4.6% | $607.76 | -1.4 | done | can't tell from luck |
| trend_filter | 566 | 48.8 | 50.4 | $-442.55 | -7.8% | $557.45 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1021 | 51.6 | 52.2 | $-519.57 | -5.1% | $480.43 | -1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 852 | 50.4 | 52.1 | $-614.59 | -7.2% | $385.41 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1021 | 48.4 | 49.6 | $-623.67 | -6.1% | $376.33 | -1.9 | done | can't tell from luck |
| coinflip | 1500 | 49.8 | 50.8 | $-849.45 | -5.7% | $150.55 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1500 | 49.6 | 51.5 | $-1090.03 | -7.3% | $-90.03 | -2.9 | done | losing for real |
| always_up | 1500 | 45.9 | 50.8 | $-1988.74 | -13.3% | $-988.74 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2307 | 47.5 | 49.4 | $-1772.69 |
| ETH | 2577 | 47.6 | 48.8 | $-1850.15 |
| SOL | 2654 | 47.8 | 49.4 | $-2036.47 |
| XRP | 2707 | 48.7 | 49.1 | $-1430.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
