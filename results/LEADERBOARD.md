# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 392 windows, 10734 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sun 12:15 AM | too few trades (196/200) |
| value_ev10 | 511 | 40.5 | 40.5 | $-158.11 | -3.1% | $841.89 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 910 | 50.8 | 49.7 | $-186.55 | -2.1% | $813.45 | -0.6 | done | can't tell from luck |
| value_ev5 | 757 | 42.0 | 42.2 | $-284.55 | -3.8% | $715.45 | -0.9 | done | can't tell from luck |
| trend_filter | 607 | 49.8 | 50.5 | $-328.76 | -5.4% | $671.24 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1080 | 49.3 | 49.7 | $-476.57 | -4.4% | $523.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1080 | 50.7 | 52.1 | $-689.04 | -6.4% | $310.96 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 910 | 49.2 | 52.2 | $-844.11 | -9.3% | $155.89 | -2.9 | done | losing for real |
| coinflip | 1561 | 49.7 | 50.8 | $-887.37 | -5.7% | $112.63 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1561 | 49.8 | 51.5 | $-1055.31 | -6.8% | $-55.31 | -2.8 | done | losing for real |
| always_up | 1561 | 46.4 | 50.7 | $-1853.41 | -11.9% | $-853.41 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2426 | 47.7 | 49.4 | $-1657.49 |
| ETH | 2706 | 47.9 | 48.9 | $-1679.56 |
| SOL | 2776 | 47.9 | 49.5 | $-2051.13 |
| XRP | 2826 | 48.9 | 49.2 | $-1402.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
