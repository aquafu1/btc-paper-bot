# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 471 windows, 12919 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1094 | 50.8 | 50.0 | $-278.93 | -2.5% | $721.07 | -0.9 | done | can't tell from luck |
| value_ev10 | 611 | 39.3 | 40.2 | $-340.10 | -5.6% | $659.90 | -1.1 | done | can't tell from luck |
| value_ev5 | 904 | 41.3 | 41.9 | $-462.79 | -5.1% | $537.21 | -1.3 | done | can't tell from luck |
| trend_filter | 750 | 49.6 | 50.8 | $-471.85 | -6.3% | $528.15 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1300 | 49.8 | 50.1 | $-527.27 | -4.1% | $472.73 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1300 | 50.2 | 51.4 | $-813.49 | -6.3% | $186.51 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1094 | 49.2 | 51.4 | $-936.21 | -8.6% | $63.79 | -2.9 | done | losing for real |
| coinflip | 1876 | 49.8 | 50.8 | $-1075.40 | -5.7% | $-75.40 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1876 | 49.7 | 51.7 | $-1375.33 | -7.3% | $-375.33 | -3.3 | done | losing for real |
| always_up | 1876 | 46.6 | 50.4 | $-2108.34 | -11.2% | $-1108.34 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2922 | 47.5 | 49.3 | $-2240.75 |
| ETH | 3237 | 48.1 | 48.8 | $-2125.93 |
| SOL | 3364 | 47.7 | 49.3 | $-2473.38 |
| XRP | 3396 | 48.7 | 49.1 | $-1674.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
