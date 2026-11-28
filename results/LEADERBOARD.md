# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1650 windows, 39370 settled trades, 390 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 838 | 34.4 | 35.2 | $-623.68 | -7.4% | $376.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3869 | 50.8 | 49.9 | $-1011.20 | -2.6% | $-11.20 | -1.6 | done | can't tell from luck |
| value_ev10 | 1979 | 38.3 | 39.0 | $-1132.71 | -5.7% | $-132.71 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3241 | 51.1 | 50.9 | $-1446.26 | -4.5% | $-446.26 | -2.6 | done | losing for real |
| value_ev5 | 2956 | 40.3 | 41.0 | $-1595.41 | -5.4% | $-595.41 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3241 | 48.9 | 49.2 | $-1812.51 | -5.6% | $-812.51 | -3.2 | done | losing for real |
| trend_filter | 2307 | 48.4 | 50.4 | $-2104.47 | -9.1% | $-1104.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3869 | 49.2 | 50.2 | $-2372.58 | -6.1% | $-1372.58 | -3.8 | done | losing for real |
| coinflip | 5690 | 49.9 | 49.9 | $-2530.63 | -4.4% | $-1530.63 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5690 | 50.2 | 51.3 | $-3543.18 | -6.2% | $-2543.18 | -4.8 | done | losing for real |
| always_up | 5690 | 48.2 | 49.0 | $-3543.25 | -6.2% | $-2543.25 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10589 | 47.9 | 48.5 | $-6000.77 |
| ETH | 11471 | 47.9 | 47.6 | $-6130.86 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
