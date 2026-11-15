# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 392 windows, 10724 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sun 12:00 AM | too few trades (196/200) |
| value_ev10 | 510 | 40.4 | 40.5 | $-169.03 | -3.3% | $830.97 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 909 | 50.8 | 49.7 | $-176.55 | -1.9% | $823.45 | -0.6 | done | can't tell from luck |
| value_ev5 | 756 | 41.9 | 42.2 | $-295.47 | -3.9% | $704.53 | -0.9 | done | can't tell from luck |
| trend_filter | 606 | 49.8 | 50.5 | $-318.76 | -5.3% | $681.24 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1079 | 49.3 | 49.7 | $-466.57 | -4.3% | $533.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1079 | 50.7 | 52.1 | $-699.95 | -6.5% | $300.05 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 909 | 49.2 | 52.2 | $-855.03 | -9.4% | $144.97 | -3.0 | done | losing for real |
| coinflip | 1560 | 49.7 | 50.8 | $-877.37 | -5.6% | $122.63 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1560 | 49.8 | 51.5 | $-1045.31 | -6.7% | $-45.31 | -2.7 | done | losing for real |
| always_up | 1560 | 46.4 | 50.7 | $-1843.41 | -11.8% | $-843.41 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2426 | 47.7 | 49.4 | $-1657.49 |
| ETH | 2696 | 48.0 | 48.9 | $-1663.23 |
| SOL | 2776 | 47.9 | 49.5 | $-2051.13 |
| XRP | 2826 | 48.9 | 49.2 | $-1402.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
